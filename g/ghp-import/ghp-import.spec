%def_with python3

Name: ghp-import
Version: 0.5.4
Release: alt1.1
Summary: Copy your docs directly to the gh-pages branch
License: Tumbolia Public License
Group: Development/Python
Url: https://pypi.python.org/pypi/ghp-import/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davisp/ghp-import.git
Source0: https://pypi.python.org/packages/f5/cd/c780b2248dd364fdc77837a020bad3e176933d7ce5643217d9475465e871/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-markdown
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-markdown
%endif

Requires: git

%description
As part of gunicorn, Benoit Chesneau and I have been starting to look at
how to host documentation. There's the obvious method of using GitHub's
post-receive hook to trigger doc builds and rsync to a webserver, but we
ended up wanting to try out github's hosting to make the whole interface
a bit more robust.

%package -n %name.py3
Summary: Copy your docs directly to the gh-pages branch
Group: Development/Python3
Requires: git

%description -n %name.py3
As part of gunicorn, Benoit Chesneau and I have been starting to look at
how to host documentation. There's the obvious method of using GitHub's
post-receive hook to trigger doc builds and rsync to a webserver, but we
ended up wanting to try out github's hosting to make the whole interface
a bit more robust.

%prep
%setup -q 

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

#pushd docs
#./build.py >index.html
#popd

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

#rm -f docs/*.py docs/*.html.tmpl

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md 
#doc docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n %name.py3
%doc *.md
#doc docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141001.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141001
- Initial build for Sisyphus

