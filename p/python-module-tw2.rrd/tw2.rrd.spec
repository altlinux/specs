%define mname tw2
%define oname %mname.rrd

%def_with python3

Name: python-module-%oname
Version: 2.1.0
Release: alt1.git20130826
Summary: tw2/rrdtool mashups! plot your rrdtool data on the web
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/tw2.rrd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toscawidgets/tw2.rrd.git
# branch: develop
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tw2.jqplugins.jqplot
BuildPreReq: python-module-tw2.jqplugins.flot
BuildPreReq: python-module-tw2.protovis.conventional
BuildPreReq: python-module-tw2.protovis.custom
BuildPreReq: python-module-tw2.protovis.hierarchies
BuildPreReq: python-module-tw2.jit python-module-pyrrd
BuildPreReq: python-module-zope.sqlalchemy python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tw2.jqplugins.jqplot
BuildPreReq: python3-module-tw2.jqplugins.flot
BuildPreReq: python3-module-tw2.protovis.conventional
BuildPreReq: python3-module-tw2.protovis.custom
BuildPreReq: python3-module-tw2.protovis.hierarchies
BuildPreReq: python3-module-tw2.jit python3-module-pyrrd
BuildPreReq: python3-module-zope.sqlalchemy python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: rrd-utils
%py_requires %mname tw2.jqplugins.jqplot tw2.jqplugins.flot
%py_requires tw2.protovis.conventional tw2.protovis.custom
%py_requires tw2.protovis.hierarchies tw2.jit pyrrd

%description
RRD (round-robin database) data visualization widgets.

You can use the widgets in this module to analyze your data from rrdtool
(usually collected by another tool like collectd or ganglia or.. well,
there are many).

%package -n python3-module-%oname
Summary: tw2/rrdtool mashups! plot your rrdtool data on the web
Group: Development/Python3
%py3_provides %oname
Requires: rrd-utils
%py3_requires %mname tw2.jqplugins.jqplot tw2.jqplugins.flot
%py3_requires tw2.protovis.conventional tw2.protovis.custom
%py3_requires tw2.protovis.hierarchies tw2.jit pyrrd

%description -n python3-module-%oname
RRD (round-robin database) data visualization widgets.

You can use the widgets in this module to analyze your data from rrdtool
(usually collected by another tool like collectd or ganglia or.. well,
there are many).

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/%mname/rrd
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%mname/rrd
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20130826
- Initial build for Sisyphus

