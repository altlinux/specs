%define oname cram

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1.hg20150104
Summary: A simple testing framework for command line applications
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/cram/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/brodie/cram
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-vim
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname

%description
Cram is a functional testing framework for command line applications
based on Mercurial's unified test format.

Cram tests look like snippets of interactive shell sessions. Cram runs
each command and compares the command output in the test with the
command's actual output.

%if_with python3
%package -n python3-module-%oname
Summary: A simple testing framework for command line applications
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Cram is a functional testing framework for command line applications
based on Mercurial's unified test format.

Cram tests look like snippets of interactive shell sessions. Cram runs
each command and compares the command output in the test with the
command's actual output.
%endif

%package -n vim-plugin-%oname-syntax
Summary: Vim syntax highlighting for Cram files
Group: Editors
BuildArch: noarch

%description -n vim-plugin-%oname-syntax
Cram is a functional testing framework for command line applications
based on Mercurial's unified test format.

Cram tests look like snippets of interactive shell sessions. Cram runs
each command and compares the command output in the test with the
command's actual output.

This package contains Cram syntax highlighting support for Vim.

%prep
%setup

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

install -d %buildroot%vim_syntax_dir
install -p -m644 contrib/*.vim %buildroot%vim_syntax_dir/

%check
python setup.py test --coverage
%if_with python3
pushd ../python3
python3 setup.py test --coverage
popd
%endif

%files
%doc *.rst *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files -n vim-plugin-%oname-syntax
%vim_syntax_dir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.hg20150104
- Initial build for Sisyphus

