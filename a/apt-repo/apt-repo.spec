Name:     apt-repo
Version:  1.1.6
Release:  alt1

Summary:  Script for manipulation APT repository list
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/apt-repo
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source:   %name-%version.tar
BuildRequires: gzip
Requires:  apt

%description
The apt-repo script allow to show, add and remove APT repositories specified
by address in sources.list(5) format, URL with optional component, branch 
name or task number.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_man1dir
install -Dpm 644 %name.8 %buildroot%_man8dir/%name.8
gzip %buildroot%_man8dir/%name.8

%find_lang %name

%files -f %name.lang
%doc TODO
%_bindir/%name
%doc %_man8dir/%name.8.gz

%changelog
* Tue Oct 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.6-alt1
- Add task source with Arepo on x86_64

* Fri Aug 30 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- Add copy:// protocol support in sources (ALT #29071)
- Fix man page:
  - Move man page to section 8 (System administration commands and daemons)
  - Fix OS name in section name (Linux instead of BSD)
  - Add copy:// protocol support
  - Remove trailing whitespace and empty lines

* Sat May 25 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- Set common key `update` for all branches for easy migration to newer
  branch because there is no branch-specific key without apt-conf update

* Thu May 23 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.3-alt1
- Add arepo 2.0 source too on adding x86_64 branch
- Show only one warning on non-existing source removal
- Add official keys for p6 and p7 brahches
- Display warning about unsupported command

* Sat Apr 27 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Add support for branches t6, p7, t7
- Use apt-repo clean instead clear

* Tue Nov 20 2012 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Add apt-repo clear command to remove all cdrom and task repositories
- Fix add cdrom source if it exist in list
- Check for wrong type on mass source deletion
- Remove error message on empty deletion

* Tue Nov 29 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Remove man page from program to separate file
- Support remove only specified type of sources
- Fix cdrom source remove

* Mon May 16 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Describe source definition in help
- Add keyword `all` in tm command to remove all active sources
- Fix use source as one string

* Mon May 09 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Make error messages more informational (closes: #25417)
- Inform about missed task number
- Show all available branch names
- Complete documentation
- Support sources.list(5) tokens in command line
- Pass all arguments as parts of source line (closes: #25418)
- Support quick forms of source: known branch name or number for task
- Fix URL for Sisyphus. Support absolute pathname for hasher repo.

* Tue Apr 19 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Fix arch definition on x86_64 (closes: #25464)

* Thu Mar 31 2011 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

