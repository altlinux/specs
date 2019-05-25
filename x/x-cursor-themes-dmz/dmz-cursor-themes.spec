Group: Graphical desktop/Other
%define oldname dmz-cursor-themes
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# FIXME: Before package was based on openSUSE package. Now it uses Debian package. Also there is git repo
# https://github.com/ganwell/dmz-cursors with high-resolution sizes. May be this is the best option?

Name:           x-cursor-themes-dmz
Version:        0.4.5
Release:        alt1_1
Summary:        Style neutral cursors themes
License:        CC-BY-SA
URL:            https://packages.debian.org/sid/gnome/dmz-cursor-theme
Source0:        http://ftp.debian.org/debian/pool/main/d/dmz-cursor-theme/dmz-cursor-theme_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  xcursorgen
Source44: import.info

%description
Scalable, style-neutral cursor themes based on the Industrial cursors designed
by Jakub Steiner for the Ximian GNOME Desktop.

%prep
%setup -q -n dmz-cursor-theme-%{version}


%build
for color in White Black; do
    cd %{_builddir}/dmz-cursor-theme-%{version}/DMZ-$color/pngs
    ./make.sh
    cd ../xcursors
    ln -s left_ptr default
    ln -s hand pointer
    ln -s left_ptr_watch progress
    ln -s watch wait
    ln -s xterm text
    ln -s dnd-link alias
    ln -s crossed_circle not-allowed
    ln -s hand1 grab
    ln -s sb_h_double_arrow col-resize
    ln -s sb_v_double_arrow row-resize
    ln -s top_side n-resize
    ln -s right_side e-resize
    ln -s bottom_side s-resize
    ln -s left_side w-resize
    ln -s top_right_corner ne-resize
    ln -s top_left_corner nw-resize
    ln -s bottom_left_corner sw-resize
    ln -s bottom_right_corner se-resize
    ln -s sb_h_double_arrow ew-resize
    ln -s sb_v_double_arrow ns-resize
    ln -s fd_double_arrow nesw-resize
    ln -s bd_double_arrow nwse-resize
    ln -s bd_double_arrow size_fdiag
    ln -s fd_double_arrow size_bdiag
    ln -s sb_h_double_arrow size_hor
    ln -s sb_v_double_arrow size_ver
    ln -s fleur size_all
done

%install
for color in White Black; do
    install -d %{buildroot}%{_datadir}/icons/DMZ-$color/cursors
    install -m644 DMZ-$color/cursor.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/index.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/xcursors/* -t %{buildroot}%{_datadir}/icons/DMZ-$color/cursors/
done

%files
%doc debian/copyright
%{_datadir}/icons/DMZ-White/
%{_datadir}/icons/DMZ-Black/

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_9
- update to new release by fcimport

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8
- moved to Sisyphus for mate-themes-extras

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6
- fc import

