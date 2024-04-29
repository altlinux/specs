%define _unpackaged_files_terminate_build 1

Name: usrmerge
Version: 0.7
Release: alt1

Summary: transition to merged usr

URL: https://altlinux.org/Usrmerge
License: MIT
Group: Other

Source: usrmerge-%version.tar

BuildRequires: make
BuildRequires: gcc

# Pull in all subpackages.
Requires: %name-hier-convert = %EVR

%description
A toolset to merge /bin, /sbin, /lib, /%_lib with their counterparts
under /usr, as safely as possible.

%prep
%setup

%build
CFLAGS="${CFLAGS:-%optflags}"; export CFLAGS;
./configure
%make_build -C out

%install
%make_install install -C out DESTDIR=%buildroot

%files
%dir %_prefix/libexec/usrmerge
%_prefix/libexec/usrmerge/mv-xchg
%_prefix/libexec/usrmerge/realpath-1

# Unfortunately, we cannot make the base package noarch and put arch-specific
# tools in a subpackage; we have to do quite the opposite.
%package hier-convert
Summary: Hierarchy conversion script
Group: System/Base
BuildArch: noarch
AutoReq: no
Requires: bash
Requires: coreutils
Requires: findutils
# Require cmp(1).
Requires: diffutils
# Require file(1) which supports file -p.
Requires: file
Requires: usrmerge = %EVR

%description hier-convert
A script which merges /bin, /sbin, /lib, /lib%_lib with their counterparts
under /usr, as safely as possible.

This package contains the script which converts the hierarchy layout.
It is intended to be called from a filetrigger or in rpm pretrans stage, but
can be invoked directly by an administrator who knows what they are doing.

%files hier-convert
%_prefix/libexec/usrmerge/hier-convert

##package block
#Summary: Install this to block installation of filesystem >= 3
#Group: Other
#BuildArch: noarch
#AutoReq: no
#Conflicts: filesystem >= 3
#
##description block
#This metapackage contains nothing. Its purpose is to keep the filesystem
#package in a system compatible with unmerged-usr, if this is temporarily
#desired on some machine.
#
##files block
#
%package ensure
Summary: Install this to convert to merged-usr
Group: Other
BuildArch: noarch
AutoReq: no
Requires(pre): usrmerge-hier-convert
# We want /proc access so usrmerge-ensure passes install check;
# its %%pre script runs hier-convert.
Requires(pre): /proc

%description ensure
This metapackage contains nothing. Its purpose is to automatically enforce the
migration to merged-usr when installed.

%files ensure

%pre ensure -p <lua>
hier_convert_prog = "%_prefix/libexec/usrmerge/hier-convert"
-- Ensure log messages are line-buffered.
os.execute("printf '%%s\n' '%name-ensure-%EVR: Starting usrmerge-hier-convert...'")
assert(os.execute(hier_convert_prog))

%changelog
* Mon Apr 29 2024 Arseny Maslennikov <arseny@altlinux.org> 0.7-alt1
- 0.6 -> 0.7; see commit history for details.
  Notably:
  + Fixed handling of certain symlinks displaced by the conversion.
- Removed the usrmerge-block subpackage. It did not work as-is anyway. :)

* Thu Apr 11 2024 Arseny Maslennikov <arseny@altlinux.org> 0.6-alt2
- Fixed output of usrmerge-ensure scripts when standard output is a file.

* Thu Apr 11 2024 Arseny Maslennikov <arseny@altlinux.org> 0.6-alt1
- 0.5 -> 0.6; see commit history for details.
  Notably:
  + Made hier-convert to call fsync(2) just after the conversion.

* Tue Apr 09 2024 Arseny Maslennikov <arseny@altlinux.org> 0.5-alt1
- 0.4 -> 0.5; see commit history for details.
  Notably:
  + Taught hier-convert to fix symlinks in unmerged dirs pointing
    to a location which usrmerge maps to itself. (Closes: 49472)
- Introduced new subpackages:
  + usrmerge-block;
  + usrmerge-ensure.

* Mon Mar 25 2024 Arseny Maslennikov <arseny@altlinux.org> 0.4-alt1
- 0.3 -> 0.4; see commit history for details.
  Notably:
  + Added a resolution rule for byte-for-byte equivalent symlinks.
    (Closes: 49533)

* Thu Feb 08 2024 Arseny Maslennikov <arseny@altlinux.org> 0.3-alt1
- 0.2 -> 0.3; see commit history for details.
  Notably:
  + Introduced new CLI flag: -f. Non-equivalent files are only
    replaced if this flag is present.
  + Added a resolution rule for byte-for-byte equivalent regular files.

* Fri Jul 28 2023 Arseny Maslennikov <arseny@altlinux.org> 0.2-alt1
- 0.1 -> 0.2; see commit history for details.
  Notably:
  + Added support for /lib32.
  + Made sure emergency cleanup is non-destructive.
  + Added various conflict resolution heuristics to hier-convert.

* Mon Jul 24 2023 Arseny Maslennikov <arseny@altlinux.org> 0.1-alt1
- Initial build.
