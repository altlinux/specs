%define _unpackaged_files_terminate_build 1
%define oname yandex_music

Name: python3-module-%oname
Version: 0.0.15
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
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%description
%summary.

%package -n %name-tests
Summary: Tests for %name
Group: Development/Python3
BuildArch: noarch
Requires: %name

%description -n %name-tests
This package contains tests for %name.

%package -n %name-docs
Summary: Docs for %name
Group: Development/Python3
BuildArch: noarch

%description -n %name-docs
This package contains docs for %name.

%prep
%setup

%build
%python3_build
pushd docs
SPHINXBUILD=sphinx-build-3 make html

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir/%oname/{docs,tests}
install -m 0644 tests/* %buildroot%python3_sitelibdir/%oname/tests
cp -pr docs/build/html %buildroot%python3_sitelibdir/%oname/docs

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%oname/docs
%exclude %python3_sitelibdir/%oname/tests
%doc LICENSE README.rst

%files -n %name-tests
%python3_sitelibdir/%oname/tests

%files -n %name-docs
%python3_sitelibdir/%oname/docs

%changelog
* Tue Dec 03 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.15-alt1
- New version

* Thu Nov 14 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.0.14-alt1
- New version
- Builded package with tests
- Builded package with docs

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
