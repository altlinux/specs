%define  modulename idna_ssl

Name:    python3-module-%modulename
Version: 1.1.0
Release: alt2

Summary: Patch ssl.match_hostname for Unicode(idna) domains support
License: MIT
Group:   Development/Python3
URL:     https://github.com/aio-libs/idna-ssl

BuildArch: noarch

Source:  %modulename-%version.tar

Packager: Anton Midyukov <antohami@altlinux.org>

%description
%summary

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%prep
%setup -n %modulename-%version
# fix requirements
sed -i 's/==/>=/g' requirements.txt
sed -i '/<=/d' requirements.txt

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.rst LICENSE

%changelog
* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt2
- rename srpm to python3-module-idna_ssl
- cleanup spec

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
