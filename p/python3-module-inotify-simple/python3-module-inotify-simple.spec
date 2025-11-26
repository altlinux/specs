%define pypi_name inotify-simple
Name:    python3-module-%pypi_name
Version: 2.0.1
Release: alt1
Summary: inotify-simple is a simple Python wrapper around inotify
License: BSD-2-Clause
URL:     https://pypi.org/project/inotify-simple
VCS:     https://github.com/chrisjbillington/inotify_simple
Source:  %name-%version.tar
Group:   Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools

%description
inotify-simple is a simple Python wrapper around inotify.
No fancy bells and whistles, just a literal wrapper with ctypes.
Less than 100 lines of code!
inotify_init1() is wrapped as a file-like object, INotify(),
holding the inotify file descriptor. INotify().read() reads available data from
the file descriptor and returns events as namedtuple objects after unpacking
them with the struct module. inotify_add_watch() and inotify_rm_watch()
are wrapped with no changes at all, taking and returning watch descriptor
integers that calling code is expected to keep track of itself,
just as one would use inotify from C. Requires Python 3.6 or higher.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README* LICENSE*
%python3_sitelibdir/__pycache__/inotify_simple.cpython-*.opt-1.pyc
%python3_sitelibdir/__pycache__/inotify_simple.cpython-*.opt-2.pyc
%python3_sitelibdir/__pycache__/inotify_simple.cpython-*.pyc
%python3_sitelibdir/inotify_simple-%version.dist-info/METADATA
%python3_sitelibdir/inotify_simple.py

%changelog
* Tue Oct 21 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 2.0.1-alt1
- Initial build.
