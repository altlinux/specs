%define _unpackaged_files_terminate_build 1
%define oname scandir

%def_without check

Name: python-module-%oname
Version: 1.10.0
Release: alt2

Summary: A better directory iterator and faster os.walk() for Python
License: BSD
Group: Development/Python
# Source-git: https://github.com/benhoyt/scandir.git
Url: https://pypi.org/project/scandir

Source: %name-%version.tar

%if_with check
BuildRequires: python-module-tox
%endif

%define long_desc scandir() is a directory iteration function like       \
os.listdir(), except that instead of returning a list of bare filenames, \
it yields DirEntry objects that include file type and stat information   \
along with the name. Using scandir() increases the speed of os.walk() by \
2-20 times (depending on the platform and file system) by avoiding       \
unnecessary calls to os.stat() in most cases.

%description
%long_desc

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build

%install
%python_install

%check
export PIP_INDEX_URL=http://host.invalid./
export LANG=en_US.utf8
tox --sitepackages -e py%{python_version_nodots python} -v

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/scandir.py*
%python_sitelibdir/_scandir.so
%python_sitelibdir/scandir-*.egg-info/

%changelog
* Wed Sep 09 2020 Stanislav Levin <slev@altlinux.org> 1.10.0-alt2
- Disabled testing.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- Initial build.

