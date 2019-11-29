%define _unpackaged_files_terminate_build 1
%define oname debug

Name: python3-module-%oname
Version: 0.3.2
Release: alt2

Summary: Start fancy debugger in a single statement
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/debug
BuildArch: noarch

# https://github.com/narfdotpl/debug.git
Source0: https://pypi.python.org/packages/19/b8/4a0021df5c30948d9c3fa1b6909afe39db3f4a612fb852997f25f4572644/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-zope

%py3_provides %oname
%py3_requires ipdb see


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

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.2-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20150331.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20150331.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150331
- Initial build for Sisyphus

