%define _unpackaged_files_terminate_build 1
%define oname argparse-manpage

%def_with check

Name: python-module-%oname
Version: 1.1
Release: alt1

Summary: Automatically build manpage from argparse
License: ASL2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/argparse-manpage/

# Source-git: https://github.com/praiskup/argparse-manpage.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(pytest)
%endif

%description
Generate manual page an automatic way from ArgumentParser object, so the
manpage 1:1 corresponds to the automatically generated -help output. The
manpage generator needs to known the location of the object, user can specify
that by (a) the module name or corresponding python filename and (b) the
object name or the function name which returns the object. There's a limited
support for (deprecated) optparse objects, too.

%package -n python3-module-%oname
Summary: Automatically build manpage from argparse
Group: Development/Python3

%description -n python3-module-%oname
Generate manual page an automatic way from ArgumentParser object, so the
manpage 1:1 corresponds to the automatically generated -help output. The
manpage generator needs to known the location of the object, user can specify
that by (a) the module name or corresponding python filename and (b) the
object name or the function name which returns the object. There's a limited
support for (deprecated) optparse objects, too.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
        mv "$i" "$i".py3
done
popd

%python_install

%check
PYTHON=python%_python_version ./check

pushd ../python3
PYTHON=python%_python3_version ./check
popd

%files
%doc LICENSE README.md
%_man1dir/argparse-manpage.1.*
%_bindir/argparse-manpage
%python_sitelibdir/argparse_manpage-%version-py%_python_version.egg-info/
%python_sitelibdir/build_manpages/

%files -n python3-module-%oname
%doc LICENSE README.md
%_man1dir/argparse-manpage.1.*
%_bindir/argparse-manpage.py3
%python3_sitelibdir/argparse_manpage-%version-py%_python3_version.egg-info/
%python3_sitelibdir/build_manpages/

%changelog
* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- Initial build.
