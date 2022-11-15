%define oname ua_parser
%def_disable check

Name: python3-module-%oname
Version: 0.4.1
Release: alt3.1
Summary: Python port of Browserscope's user agent parser
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/ua-parser/

# https://github.com/tobie/ua-parser.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python3-module-yaml

%py3_provides %oname

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/user_agent_parser.py

%description
The crux of the original parser--the data collected by Steve Souders
over the years--has been extracted into a separate YAML file so as to be
reusable as is by implementations in other programming languages.

ua-parser is just a small wrapper around this data.

%prep
%setup

cp -v regexes.* uap-core/
cp -v regexes.* py/ua_parser/

%build
%python3_build

%install
%python3_install
install -m644 py/%oname/regexes.* %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test

%files
%doc *.md *.txt *.markdown
%python3_sitelibdir/*

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.4.1-alt3.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt3
- Drop python2 support.

* Thu Jan 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt2
- NMU: Updated build dependencies.

* Tue May 30 2017 Lenar Shakirov <snejok@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 0.3.4-alt3.git20141025
- Enable python3

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.4-alt2.git20141025
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20141025
- Initial build for Sisyphus

