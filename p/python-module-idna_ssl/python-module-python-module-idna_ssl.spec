%define  modulename idna_ssl

Name:    python-module-%modulename
Version: 1.1.0
Release: alt1

Summary: Patch ssl.match_hostname for Unicode(idna) domains support
License: MIT
Group:   Development/Python
URL:     https://github.com/aio-libs/idna-ssl

BuildArch: noarch

Source:  %modulename-%version.tar

Packager: Anton Midyukov <antohami@altlinux.org>

%description
%summary

%package -n python3-module-%modulename
Summary: Patch ssl.match_hostname for Unicode(idna) domains support
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description -n python3-module-%modulename
%summary

%prep
%setup -n %modulename-%version
# fix requirements
sed -i 's/==/>=/g' requirements.txt
sed -i '/<=/d' requirements.txt

%build
%python3_build

%install
%python3_install

%files -n python3-module-%modulename
%python3_sitelibdir/*
%doc *.rst LICENSE

%changelog
* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
