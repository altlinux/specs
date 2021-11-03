%def_without terminal_solution

Name: evilwm
Version: 1.3.1
Release: alt0.1

Summary: a minimalist window manager derived from aewm
License: BSD-like
Group: Graphical desktop/Other
Url: http://www.6809.org.uk/evilwm/
Vcs: https://github.com/mati75/evilwm.git

Source: %url/%name-%version.tar.gz

# debian patches (1.3.1-1)
Patch0: remove-encoding.patch
Patch1: show-in-login-manager.patch
Patch2: enable_hardening.patch
Patch3: drop_build_pdf.patch

Patch10: evilwm-0.99.24-alt-center-placement.patch
Patch11: evilwm-1.0.0-alt-supermini.patch

# Added by buildreq2 on Fri Mar 31 2006
BuildRequires: libXext-devel libXrandr-devel libXrender-devel

%description
%name is a minimalist window manager for the X Window System.

%name features include:
* No window decorations apart from a simple 1 pixel border.
* No icons.
* Good keyboard control, including repositioning and maximise toggles.
* Virtual desktops.

%prep
%setup

%if_with terminal_solution
# center-placement.patch
%patch10 -p1
# supermini.patch
%patch11 -p2
%endif

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%make

%install
%make_install DESTDIR=%buildroot install

# for now, evilwm is not ready for public xsessions.
# it needs at least a script like startevilwm
# that launches services nessesary for a modern x session,
# something like a script in doc/xsession.txt

#mv %buildroot%_datadir/{applications,xsessions}
rm -rf %buildroot%_datadir/applications

%files
%_bindir/%name
%_man1dir/%name.*
#%_datadir/xsessions/%name.desktop

%changelog
* Wed Nov 03 2021 Igor Vlasenko <viy@altlinux.org> 1.3.1-alt0.1
- NMU: new version 1.3.1

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1
- NMU: new version 1.1.1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.1-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Tue Mar 22 2011 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- New version

* Tue Mar 22 2011 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt2
- Updated build dependencies

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1.1
- NMU:
  * updated build dependencies

* Tue Jul 10 2007 Alex V. Myltsev <avm@altlinux.ru> 1.0.0-alt1
- New version: basic XRandr support, fixes re maximizing and snapping.

* Thu Jul 20 2006 Alex V. Myltsev <avm@altlinux.ru> 0.99.25-alt1
- New version: bug fixes re virtual desktops and keyboard grabs.

* Fri Mar 31 2006 Alex V. Myltsev <avm@altlinux.ru> 0.99.24-alt1
- Initial build for Sisyphus

