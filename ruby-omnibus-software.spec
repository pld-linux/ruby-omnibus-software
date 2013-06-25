%define	pkgname	omnibus-software
Summary:	Open Source Software for use in Omnibus built packages
Name:		ruby-%{pkgname}
Version:	0.0.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://github.com/opscode/omnibus-software/tarball/master?/%{pkgname}-%{version}.tgz
# Source0-md5:	10d12731173e0226a6efb35e2be04599
URL:		https://github.com/opscode/omnibus-software
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-rake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared software descriptions, for use by any Omnibus project that
needs them.

%prep
%setup -qc
mv *-%{pkgname}-*/* .

%build
# produce .gem first and extract it
rake build
%{__tar} -xmf pkg/%{pkgname}-%{version}.gem

%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -d $RPM_BUILD_ROOT%{ruby_gemdir}/gems/%{pkgname}-%{version}
cp -a config $RPM_BUILD_ROOT%{ruby_gemdir}/gems/%{pkgname}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_gemdir}/gems/%{pkgname}-%{version}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
