%define _unpackaged_files_terminate_build 1

Name: grako
Version: 3.99.9
Release: alt1

Summary: Grako (for grammar compiler).
License: BSD
Group: Sciences/Other
URL: https://pypi.org/project/grako/
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest-runner

Requires: python3-module-%name = %EVR
%py3_requires pygraphviz


%description
Grako is a tool that takes grammars in a variation of EBNF as input, and
outputs memoizing (Packrat) PEG parsers in Python.

Grako can also compile a grammar stored in a string into a Grammar object that
can be used to parse any given input, much like the re module does with regular
expressions.

%package -n python3-module-%name
Summary: A python module for %name
Group: Development/Python3

%description -n python3-module-%name
Grako is a tool that takes grammars in a variation of EBNF as input, and
outputs memoizing (Packrat) PEG parsers in Python.

Grako can also compile a grammar stored in a string into a Grammar object that
can be used to parse any given input, much like the re module does with regular
expressions.

This package contains python3 module for %name.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.99.9-alt1
- Initial build for Sisyphus

