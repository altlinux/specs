Name:		patchdeps
Version:	0.1
Release:	alt1.1
Group:		Text tools
License:	MIT
Source:		%name-%version.tar
URL:		https://github.com/matthijskooijman/patchdeps
Summary:	Analyzing textual dependencies within a patch series
BuildPreReq:	rpm-build-python3
BuildArch:	noarch

%description
Given a pile of patches, `patchdeps` can find out which patch modifies
which files and lines within those files. From there, it can detect that
a specific patch modifies a line introduced by an earlier patch, and
mark these patches as dependent.

This tool is intended to sort out a pile of patches, so you can
determine which patches should be applied together as a group and which
can be freely reordered without problems.

%prep
%setup
sed -i "
/from parser import parse_diff/r parser.py
/from parser import/d
s/'xdot'/'dotty'/g
" patchdeps.py

%install
install -D -m755 patchdeps.py %buildroot%_bindir/patchdeps

%files
%doc README*
%_bindir/patchdeps

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 23 2014 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build

