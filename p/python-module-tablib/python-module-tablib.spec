
%def_with python3
%define modname tablib

Name:		python-module-%modname
Version:	0.10.0
Release:	alt1.1
Summary:	Format agnostic tabular data library (XLS, JSON, YAML, CSV)

Group:		Development/Python
License:	MIT
URL:		http://github.com/kennethreitz/tablib
Source0:	%name-%version.tar

BuildArch:	noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-jinja2 python-module-mccabe python-module-pbr python-module-pyasn1 python-module-pytz python-module-setuptools python-module-simplejson python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python-tools-pep8 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-chardet python-module-docutils python-module-hacking python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-yaml python3-module-html5lib python3-module-pbr python3-module-yaml rpm-build-python3 time

#BuildRequires:    python-devel
#BuildRequires:    python-module-setuptools
#BuildRequires:    python-module-pbr
#BuildRequires:    python-module-yaml
#BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:    python-tools-2to3
#BuildRequires:    python3-devel
#BuildRequires:    python3-module-setuptools
#BuildRequires:    python3-module-pbr
#BuildRequires:    python3-module-yaml
%endif

%description
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)

%package -n python3-module-%modname
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)
Group:            Development/Python3

%add_python3_req_skip UserDict
%add_python3_req_skip odf

%description -n python3-module-%modname
Tablib is a format-agnostic tabular dataset library, written in Python.

Output formats supported:

 - Excel (Sets + Books)
 - JSON (Sets + Books)
 - YAML (Sets + Books)
 - HTML (Sets)
 - TSV (Sets)
 - CSV (Sets)

%prep
%setup

# Remove shebangs
for lib in $(find . -name "*.py"); do
 sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%if_with python3
cp -fR . ../python3
pushd ../python3
sed -i "/\(xlwt\|odf\|xlrd\|openpyxl\|openpyxl\..*\|yaml\)'/d" setup.py
find . -name "*.py" | grep -v 3 | xargs 2to3 -w
popd
%endif

sed -i '/tablib.packages.*3/d' setup.py

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst AUTHORS LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modname
%doc README.rst AUTHORS LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- cleanup spec
- python3 package

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.11.20120702git752443f-alt1
- Initial release for Sisyphus (based on Fedora)
