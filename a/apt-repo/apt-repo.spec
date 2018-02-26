Name:     apt-repo
Version:  1.1.0
Release:  alt1

Summary:  Script for manipulation APT repository list
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/apt-repo
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source: %name-%version.tar
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
install -Dpm 644 %name.1 %buildroot%_man1dir/%name.1
gzip %buildroot%_man1dir/%name.1

%find_lang %name

%files -f %name.lang
%doc TODO
%doc %_man1dir/*
%_bindir/%name
%doc %_man1dir/%{name}*

%changelog
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

