%define _unpackaged_files_terminate_build 1
%define pypi_name flit
%define pypi_name_core flit-core

%def_with check

Name: python3-module-%pypi_name
Version: 3.7.1
Release: alt1
Summary: A simple packaging tool for simple packages
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/flit/
VCS: https://github.com/pypa/flit

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# deps
BuildRequires: python3(requests)
BuildRequires: python3(docutils)
BuildRequires: python3(tomli-w)

BuildRequires: python3(pytest)
BuildRequires: python3(testpath)
BuildRequires: python3(responses)
BuildRequires: python3(tomli)
%endif

%description
Flit is a simple way to put Python packages and modules on PyPI. It tries to
require less thought about packaging and help you avoid common mistakes

%package -n python3-module-%pypi_name_core
Summary: Distribution-building parts of Flit
License: BSD
Group: Development/Python3
# previously flit_core was a part of flit
Conflicts: python3-module-flit <= 3.6.0
%py3_provides %pypi_name_core

%description -n python3-module-%pypi_name_core
Distribution-building parts of Flit.

%prep
%setup
%autopatch -p1

%build
# build PEP517 backend
pushd flit_core
%pyproject_build
popd

# actually it should be built with self-hosted backend
export PYTHONPATH=$(pwd)/flit_core
%pyproject_build

%install
pushd flit_core
%pyproject_install
popd
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/flit_core/tests/

%check
%tox_check_pyproject

%files
%doc LICENSE
%doc README.rst
%_bindir/flit
%python3_sitelibdir/flit/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-%pypi_name_core
%python3_sitelibdir/flit_core/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name_core}/

%changelog
* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- 3.6.0 -> 3.7.1.
- Subpackaged PEP517 build backend (flit_core).

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1
- Updated to upstream version 3.6.0.

* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Tue Jun 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Disabled bootstrapping.

* Mon Aug 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 0.9-5
- Use python install wheel macro

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9-3
- Updated spec file with license comments and provides

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9-2
- spec file cleanup

* Sat Jul 2 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.9-1
- Initial RPM release
