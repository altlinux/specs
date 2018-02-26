Name: rpm-macros-make
Version: 0.1
Release: alt1

Summary: Make helper macros to rebuild packages
License: GPL
Group: Development/Other
Url: http://www.altlinux.org/

Source: %name-%version.tar
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description
This is extended make macros: %%make_build_ext for parallel build,
%%make_ext for sequential build.
Standard flags defined, but may changed with %%add_optflags.

%prep
%setup

%install
install -pD -m644 make %buildroot%_rpmmacrosdir/make

%files
%_rpmmacrosdir/*

%changelog
* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

