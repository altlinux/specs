Summary: Freedesktop compliant Window Manager common requirements.
Name: wm-common-freedesktop
Version: 1.3
Release: alt1
License: GPL2+ or Artistic
Group: Graphical desktop/Other
Packager: Igor Vlasenko <viy@altlinux.ru>
URL: http://wiki.altlinux.org/WMPackagingPolicy
BuildArch: noarch

Requires: desktop-file-utils shared-mime-info xdg-utils url_handler altlinux-mime-defaults
# added automatically when needed
# Requires: xinitrc

%description
wm-common-freedesktop is the set of prerequisites 
a freedesktop compliant Window Manager must have. 
It includes dependecies for desktop, mime database
and xdg-utils.

The point is that packages that has freedesktop DE/WM-specific resources 
such as icons or .desktop files should not require corresponding 
freedesktop utilities such as desktop-file-utils. 
Instead, the packages that are capable to utilize those resources
(namely, Window Managers and Desktop Environments) should have
a single requirement to wm-common-freedesktop.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir

%files 

%changelog
* Thu Apr 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- added altlinux-mime-defaults

* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- added url_handler according to the new menu policy.

* Thu Jun 17 2010 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- added xdg-utils

* Fri Mar 06 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- build for Sisyphus.

* Sat Sep 13 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.5
- initial build for Daedalus
