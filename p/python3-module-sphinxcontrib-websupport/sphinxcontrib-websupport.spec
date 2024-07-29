%define oname sphinxcontrib-websupport

%def_with check

Name:           python3-module-%oname
Version:        2.0.0
Release:        alt1
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
Group:          Development/Python3
URL:            https://pypi.org/project/sphinxcontrib-websupport
VCS:            https://github.com/sphinx-doc/sphinxcontrib-websupport

BuildArch:      noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-sphinx-tests
%endif

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/sphinxcontrib/websupport
%python3_sitelibdir/sphinxcontrib_websupport-%{version}.dist-info

%changelog
* Mon Jul 29 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt1
- Automatically updated to 1.2.7.
- Built with check.

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.4-alt2
- Fixed build.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.4-alt1
- Updated to upstream version 1.2.4.

* Mon Sep 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt1
- Updated to upstream version 1.1.2.
- Built without support for python-2.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3.qa1
- NMU: applied repocop patch

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt3
- (NMU) rebuild with python3.6

* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2
- Rebuild with new setuptools to fix namespace package

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.

* Wed Oct 11 2017 Troy Dawson <tdawson@redhat.com> - 1.0.1-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Javier Peña <jpena@redhat.com> - 1.0.1-1
- Initial package.
