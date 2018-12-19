%define _unpackaged_files_terminate_build 1
%global oname pathlib2

%def_with check

Name: python-module-%oname
Version: 2.3.3
Release: alt1

Summary: Object-oriented filesystem paths
License: MIT
Group: Development/Python

# Source-git: https://github.com/mcmtroffaes/pathlib2
Url: https://pypi.org/project/pathlib2
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-test
BuildRequires: python-module-scandir
BuildRequires: python-module-mock
BuildRequires: python-module-pytest
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch
%py_requires scandir

%global _description \
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%description %_description
%package -n python3-module-%oname
Group: Development/Python
Summary: %summary

%description -n python3-module-%oname %_description

%prep
%setup
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
PYTHONPATH=. py.test -v tests

pushd ../python3
PYTHONPATH=. py.test3 -v tests
popd

%files
%doc CHANGELOG.rst LICENSE.rst README.rst
%python_sitelibdir/pathlib2/
%python_sitelibdir/pathlib2-*.egg-info/

%files -n python3-module-%oname
%doc CHANGELOG.rst LICENSE.rst README.rst
%python3_sitelibdir/pathlib2/
%python3_sitelibdir/pathlib2-*.egg-info/

%changelog
* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 2.3.3-alt1
- 2.3.2 -> 2.3.3.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 2.3.2-alt1
- 2.1.0 -> 2.3.2.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt3
- Fixed build dependencies.

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt2
- Updated build spec.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
