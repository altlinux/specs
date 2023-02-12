Name:     setbranding
Version:  1.1.4
Release:  alt1

Summary:  Script for manipulation ALT Linux branding packages
License:  GPLv3+
Group:    System/Configuration/Packaging
URL:      http://altlinux.org/setbranding
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source:   setbranding

Requires: apt make-initrd
%add_findreq_skiplist %_bindir/%name

%description
Script for manipulation ALT Linux branding (distribution design profile)
packages. You can show installed branding packages and switch to other
branding.

%install
install -Dm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sun Feb 12 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- skips grub setup if can't access it with root (thanks onetowne@yandex.ru) (ALT #44280)

* Wed Feb 27 2019 Anton Midyukov <antohami@altlinux.org> 1.1.3-alt1
- fix build for non-x86 (closes: 36139)

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- Remove path from rpm

* Tue Oct 08 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Abort script on apt-get interrupt
- Support verbose output
- Ignore switch to already used branding

* Tue Sep 10 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Add -l option for display list of all available brandings

* Thu Aug 08 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Set full path to programs
- Check root privileges on branding change
- Show usage information
- Update grub on branding change

* Wed Aug 07 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus

