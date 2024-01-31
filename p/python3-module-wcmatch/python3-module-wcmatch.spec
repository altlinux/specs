Name: python3-module-wcmatch
Version: 8.5
Release: alt1
Summary: Wilcard File Name matching library
License: MIT
Group: Development/Python3
Url: https://github.com/facelessuser/wcmatch.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel >= 3.8
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling python3-module-bracex >= 2.1.1

# for tests
BuildRequires: python3-module-pytest

%description
Wildcard Match provides an enhanced fnmatch, glob, and pathlib library in order
to provide file matching and globbing that more closely follows the features
found in Bash. In some ways these libraries are similar to Python's builtin
libraries as they provide a similar interface to match, filter, and glob
the file system. But they also include a number of features found in Bash's
globbing such as backslash escaping, brace expansion, extended glob pattern groups, etc.
They also add a number of new useful functions as well, such as globmatch
which functions like fnmatch, but for paths.

Wildcard Match also adds a file search utility called wcmatch that
is built on top of fnmatch and globmatch. It was originally written for Rummage,
but split out into this project to be used by other projects that
may find its approach useful.

Bash is used as a guide when making decisions on behavior for fnmatch and glob.
Behavior may differ from Bash version to Bash version, but an attempt is made
to keep Wildcard Match up with the latest relevant changes. With all of this said,
there may be a few corner cases in which we've intentionally chosen to not exactly mirror Bash.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.md README.md
%python3_sitelibdir/*

%changelog
* Tue Jan 30 2024 Alexey Shabalin <shaba@altlinux.org> 8.5-alt1
- Initial build.

