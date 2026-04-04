Name:  adaptix
Version: 3.0.0
Release: alt5

Summary: An extremely flexible and configurable data model conversion library.
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/adaptix/
Vcs: https://github.com/reagento/adaptix

BuildArch: noarch

Source0: %name-%version.tar
Source1: release_data.tar

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-uv-build

%description
%summary

%package -n python3-module-%name
Group:  Development/Python3
Summary: An extremely flexible and configurable data model conversion library.

%description -n python3-module-%name
%summary

%package -n python3-module-%name-examples
Group:  Development/Python3
Summary: Examples for adaptix.
AutoProv: nopython3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-examples
%summary

%package -n python3-module-%name-tests
Group:  Development/Python3
Summary: Tests for adaptix.
AutoProv: nopython3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-tests
%summary

%package -n python3-module-tests_helpers
Group:  Development/Python3
Summary: tests helpers for adaptix

%description -n python3-module-tests_helpers
%summary


%prep
%setup
tar -xf %SOURCE1 -C benchmarks/

%build
%pyproject_build
pushd tests/tests_helpers/
%pyproject_build
popd

%install
%pyproject_install

cp -r -p examples %buildroot%python3_sitelibdir/%name/
cp -r -p tests %buildroot%python3_sitelibdir/%name/
mv %buildroot%python3_sitelibdir/%name/tests/tests_helpers/tests_helpers %buildroot%python3_sitelibdir/
rm  -r %buildroot%python3_sitelibdir/%name/tests/tests_helpers

%files -n python3-module-%name
%doc LICENSE *.md
%exclude %python3_sitelibdir/%name/tests
%exclude %python3_sitelibdir/%name/examples
%python3_sitelibdir/%name/
%python3_sitelibdir/adaptix-3.0.0b12.dist-info/

%files -n python3-module-%name-examples
%python3_sitelibdir/%name/examples

%files -n python3-module-%name-tests
%python3_sitelibdir/%name/tests

%files -n python3-module-tests_helpers
%python3_sitelibdir/tests_helpers

%changelog
* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt5
- update git.03ef02f823 (version 3.0.0b12)

* Sat May 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt4
- update git.0e4132507c (version 3.0.0b11)

* Mon Apr 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt3
- update git.9c8606c1bf (version 3.0.0b10)

* Sat Feb 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt2
- rebuild with removed %%add_python3_path

* Tue Jan 14 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt1
- Initial build (version 3.0.0b9).
