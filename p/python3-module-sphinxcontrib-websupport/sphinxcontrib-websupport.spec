%define _unpackaged_files_terminate_build 1

%define oname sphinxcontrib-websupport

Name:           python3-module-%oname
Version:        1.2.4
Release:        alt2
Summary:        Sphinx API for Web Apps
License:        BSD
Group:          Development/Python3
URL:            http://sphinx-doc.org/

BuildArch:      noarch

# https://github.com/sphinx-doc/sphinxcontrib-websupport.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/sphinxcontrib/websupport
%python3_sitelibdir/sphinxcontrib_websupport-%{version}*-py3.*-*.pth
%python3_sitelibdir/sphinxcontrib_websupport-%{version}*-py3.*.egg-info

%changelog
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
