%define oname sphinxcontrib_github_alt

%def_without python3

Name:           python-module-%oname
Version:        1.0
Release:        alt4
Summary:        Github roles for Sphinx docs
Group:          Development/Python
License:        BSD
URL:            https://github.com/jupyter/sphinxcontrib_github_alt
BuildArch:      noarch

# https://github.com/jupyter/sphinxcontrib_github_alt.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%description
Link to GitHub issues, pull requests, commits and users for a particular project.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Github roles for Sphinx docs

%description -n python3-module-%oname
Link to GitHub issues, pull requests, commits and users for a particular project.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build

%install
install -pD -m644 sphinxcontrib_github_alt.py %buildroot%python_sitelibdir/sphinxcontrib_github_alt.py

%if_with python3
pushd ../python3
install -pD -m644 sphinxcontrib_github_alt.py %buildroot%python3_sitelibdir/sphinxcontrib_github_alt.py
popd
%endif

%files
%doc README.rst COPYING.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst COPYING.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt4
- Rebuilt without python-3.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa1
- NMU: applied repocop patch

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- (NMU) rebuild with python3.6

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT.
