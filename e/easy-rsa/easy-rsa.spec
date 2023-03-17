Name: easy-rsa
Version: 3.1.2
Release: alt1

Summary: Simple shell based CA utility
Group: Security/Networking
License: %gpl2only
Url: https://github.com/OpenVPN/easy-rsa
Packager: Vladimir Didenko <cow@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-licenses
Requires: openssl

%description
easy-rsa is a CLI utility to build and manage a PKI CA. In laymen's terms,
this means to create a root certificate authority, and request and sign
certificates, including sub-CAs and certificate revokation lists (CRL).

%prep
%setup -q
%patch0 -p1

%build
mkdir -p %{buildroot}%{_datadir}/%name
mkdir -p %{buildroot}%{_bindir}
cp -r easyrsa3/* %{buildroot}%{_datadir}/%name
mv %{buildroot}%{_datadir}/%name/easyrsa %{buildroot}%{_bindir}/

%files
%defattr(-,root,root,-)
%doc COPYING.md doc/ ChangeLog README.md README.quickstart.md KNOWN_ISSUES
%{_bindir}/easyrsa
%{_datadir}/%name

%changelog
* Fri Mar 17 2023 Vladimir Didenko <cow@altlinux.org> 3.1.2-alt1
- new version

* Tue Oct 18 2022 Vladimir Didenko <cow@altlinux.org> 3.1.1-alt1
- new version

* Fri Jun 10 2022 Vladimir Didenko <cow@altlinux.org> 3.1.0-alt1
- new version

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 3.0.8-alt1
- new version

* Fri Apr 10 2020 Vladimir Didenko <cow@altlinux.org> 3.0.7-alt1
- new version

* Wed Mar 6 2019 Vladimir Didenko <cow@altlinux.org> 3.0.6-alt1
- new version

* Wed Jul 25 2018 Vladimir Didenko <cow@altlinux.org> 3.0.4-alt1
- new version

* Wed Jul 27 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt2
- v3.0.0-16-g5a429d2

* Wed Jun 17 2015 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
