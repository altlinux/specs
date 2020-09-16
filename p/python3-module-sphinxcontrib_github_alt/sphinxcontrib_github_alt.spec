%define oname sphinxcontrib_github_alt

Name:           python3-module-%oname
Version:        1.2
Release:        alt1
Summary:        Github roles for Sphinx docs
Group:          Development/Python3
License:        BSD-2-Clause
URL:            https://github.com/jupyter/sphinxcontrib_github_alt

BuildArch:      noarch

# https://github.com/jupyter/sphinxcontrib_github_alt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%description
Link to GitHub issues, pull requests, commits and users for a particular project.

%prep
%setup

%build
flit build

%install
pip%{_python3_version} install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%files
%doc COPYING.md
%doc README.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream version 1.2.
- Disabled build for python-2.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa1
- NMU: applied repocop patch

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- (NMU) rebuild with python3.6

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT.
