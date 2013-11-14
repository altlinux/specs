Name: elementary-os
Version: 1
Release: alt7

Summary: Elementary OS
Group: Graphical desktop/Other
License: Free
Url: http://elementaryos.org/

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

# watchdog
Requires: cerbere

Requires: contractor

# icons
Requires: elementary-icon-theme

# IM
Requires: empathy

# email client
Requires: geary

# web browser
Requires: midori

# music player
Requires: noise

# file manager
Requires: pantheon-files

# dropbox integration for pantheon-files
Requires: pantheon-files-plugin-dropbox

# terminal
Requires: pantheon-terminal

# text editor
Requires: scratch-text-editor

# for images
Requires: shotwell

# top panel
Requires: wingpanel

Requires: libpantheon

%description
Elementary OS.

%prep

%files

%changelog
* Thu Nov 14 2013 Igor Zubkov <icesik@altlinux.org> 1-alt7
- Add libpantheon to requires

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 1-alt6
- Add wingpanel to requires

* Sun Sep 15 2013 Igor Zubkov <icesik@altlinux.org> 1-alt5
- Add pantheon-files-plugin-dropbox to requires

* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 1-alt4
- Add noise to requires

* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 1-alt3
- Add contractor to requires
- Add empathy to requires
- Add shotwell to requires

* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 1-alt2
- Add cerbere to requires

* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 1-alt1
- build for Sisyphus

