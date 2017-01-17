%define _unpackaged_files_terminate_build 1
%define oname debug

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1
Summary: Start fancy debugger in a single statement
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/debug
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/narfdotpl/debug.git
Source0: https://pypi.python.org/packages/19/b8/4a0021df5c30948d9c3fa1b6909afe39db3f4a612fb852997f25f4572644/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ipdb python-module-see
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ipdb python3-module-see
%endif

%py_provides %oname
%py_requires ipdb see

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-module-zope rpm-build-python3

%description
Start fancy debugger in a single statement.

People debug with print. It's great in simple cases. Another debugging
tool, pdb, is less popular as it requires more effort: one has to do a
Google search, skim through documentation, type some long "trace...
sth", and all of this only to get some unfriendly two-color shell that
doesn't even seem to understand how tab key should work.

This project FTFY: you import debug and you find yourself in a debugger
with syntax highlighting, tab completion, and readable dir()
alternative. From there you can pretend you're just using interactive
console -- you don't have to know any pdb commands, just remember that
"c" closes debugger and goes back to your program.

(What really happens is that we simply start ipdb and import see for
you.)

%if_with python3
%package -n python3-module-%oname
Summary: Start fancy debugger in a single statement
Group: Development/Python3
%py3_provides %oname
%py3_requires ipdb see

%description -n python3-module-%oname
Start fancy debugger in a single statement.

People debug with print. It's great in simple cases. Another debugging
tool, pdb, is less popular as it requires more effort: one has to do a
Google search, skim through documentation, type some long "trace...
sth", and all of this only to get some unfriendly two-color shell that
doesn't even seem to understand how tab key should work.

This project FTFY: you import debug and you find yourself in a debugger
with syntax highlighting, tab completion, and readable dir()
alternative. From there you can pretend you're just using interactive
console -- you don't have to know any pdb commands, just remember that
"c" closes debugger and goes back to your program.

(What really happens is that we simply start ipdb and import see for
you.)
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20150331.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20150331.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150331
- Initial build for Sisyphus

