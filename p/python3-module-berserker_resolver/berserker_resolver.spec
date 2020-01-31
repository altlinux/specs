%define oname berserker_resolver

Name:       python3-module-%oname
Version:    2.0.1
Release:    alt2

Summary:    Fast mass dns resolver which can bypass loadbalancers
License:    BSD
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/berserker_resolver/

BuildArch:   noarch

# https://github.com/DmitryFillo/berserker_resolver.git
Source:     %name-%version.tar
Patch1:     %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-dns python3-module-mock

%py3_provides %oname
%py3_requires dns


%description
Berserker Resolver is fast mass dns resolver which can bypass
loadbalancers.

%prep
%setup
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst TODO
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1
- Updated to upstream version 2.0.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20141125
- Initial build for Sisyphus

