Name: elementary-os
Version: 1
Release: alt2

Summary: Elementary OS
Group: Graphical desktop/Other
License: Free
Url: http://elementaryos.org/

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

# watchdog
Requires: cerbere

# icons
Requires: elementary-icon-theme

# email client
Requires: geary

# web browser
Requires: midori

# file manager
Requires: pantheon-files

# terminal
Requires: pantheon-terminal

# text editor
Requires: scratch-text-editor

%description
Elementary OS.

%prep

%files

%changelog
* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 1-alt2
- Add cerbere to requires

* Tue Sep 10 2013 Igor Zubkov <icesik@altlinux.org> 1-alt1
- build for Sisyphus

