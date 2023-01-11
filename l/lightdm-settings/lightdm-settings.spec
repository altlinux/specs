Name: lightdm-settings
Version: 1.6.1
Release: alt1
Summary: Configuration tool for the LightDM display manager
Group: Graphical desktop/Other
License: GPLv3+
Url: https://github.com/linuxmint/lightdm-settings
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

BuildPreReq: rpm-build-python3
Requires: slick-greeter
Requires: python3(xapp)
Requires: python3(setproctitle)
Requires: python3-module-pygobject3

%description
This tool currently lets users configure slick-greeter.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
# No install target in Makefile
install -m755 -pd %{buildroot}
cp -pr .%{_prefix} %{buildroot}

# Set exec permissions for bin/* files.
chmod -c 0755 %{buildroot}%{_bindir}/%{name}			\
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

%find_lang %{name}


%files -f %name.lang
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy

%changelog
* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Nov 21 2022 Vladimir Didenko <cow@altlinux.org> 1.5.10-alt1
- 1.5.10

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 1.5.9-alt1
- 1.5.9

* Wed Jul 13 2022 Vladimir Didenko <cow@altlinux.org> 1.5.8-alt1
- 1.5.8

* Thu Jan 13 2022 Vladimir Didenko <cow@altlinux.org> 1.5.7-alt1
- 1.5.7

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 1.5.6-alt1
- 1.5.6

* Tue Jun 29 2021 Vladimir Didenko <cow@altlinux.org> 1.5.5-alt1
- 1.5.5

* Thu Jun 17 2021 Vladimir Didenko <cow@altlinux.org> 1.5.4-alt1
- 1.5.4

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.org> 1.5.3-alt1
- 1.5.3

* Wed May 5 2021 Vladimir Didenko <cow@altlinux.org> 1.5.2-alt2
- add rpm-build-python3 to the build requirements

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 1.5.2-alt1
- 1.5.2

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 1.5.1-alt1
- 1.5.1

* Thu Dec 3 2020 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- 1.5.0

* Fri Jun 23 2020 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Jan 8 2020 Vladimir Didenko <cow@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 1.3.2-alt1
- 1.3.2

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 1.3.1-alt1
- 1.3.1

* Mon Nov 25 2019 Vladimir Didenko <cow@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Aug 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.8-alt1
- 1.2.8

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 1.2.7-alt1
- 1.2.7

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.6-alt1
- 1.2.6

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 1.2.4-alt1
- 1.2.4

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jun 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 18 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.1.4-alt1
- 1.1.4

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Sep 4 2017 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
