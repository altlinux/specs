%define _unpackaged_files_terminate_build 1
%define oname yandex_music

Name: python3-module-%oname
Version: 0.0.12
Release: alt1
Summary: Unofficial library for Yandex.Music API
License: LGPLv3
Group: Development/Python3
Url: https://github.com/MarshalX/yandex-music-api
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary.


%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir/%oname/{docs,examples}
cp -R docs/* %buildroot%python3_sitelibdir/%oname/docs
cp -R examples/* %buildroot%python3_sitelibdir/%oname/examples

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%{_python3_version}.egg-info
%doc LICENSE README.*

%changelog
* Wed Sep 18 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.12-alt1
- New version

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.10-alt1
- New version

* Sat Aug 24 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.9-alt1
- New version

* Sun Jul 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.5-alt2
- Minor spec fix

* Wed Jul 17 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.5-alt1
- New version

* Tue Jul 16 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.4-alt1
- Initial build for ALT
