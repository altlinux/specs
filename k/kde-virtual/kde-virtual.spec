%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kde-virtual
Version: 6.0.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Virtual packages for KDE
Url: https://www.altlinux.org/
License: ALT-Public-Domain

#BuildArch: noarch

BuildRequires(pre): rpm-macros-qt6-webengine

%description
%summary

%package -n kde-network-manager-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy network manager
Provides: kde5-network-manager-0-dummy = %EVR
Obsoletes: kde5-network-manager-0-dummy < %EVR
#
Provides: kde-network-manager = %EVR
Provides: kde-network-manager-dummy = %EVR
Requires: kde-common
%description -n kde-network-manager-0-dummy
%summary

%package -n kde-network-manager-2-etcnet
Group: Graphical desktop/KDE
Summary: /etc/net network manager
Provides: kde5-network-manager-2-etcnet = %EVR
Obsoletes: kde5-network-manager-2-etcnet < %EVR
#
Provides: kde-network-manager = %EVR
Provides: kde-network-manager-etcnet = %EVR
Requires: kde-common
Requires: etcnet alterator-net-wifi alterator-net-openvpn alterator-net-pppoe alterator-net-pptp alterator-net-l2tp
%description -n kde-network-manager-2-etcnet
%summary

%package -n kde-network-manager-4-nm
Group: Graphical desktop/KDE
Summary: NetworkManager network manager
Provides: kde5-network-manager-4-nm = %EVR
Obsoletes: kde5-network-manager-4-nm < %EVR
Provides: kde5-network-manager-nm = %EVR
#
Provides: kde-network-manager = %EVR
Provides: kde-network-manager-nm = %EVR
Requires: kde-common
Requires: plasma-nm-maxi
%description -n kde-network-manager-4-nm
%summary

%package -n kde-video-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy video player
Provides: kde5-video-player-0-dummy = %EVR
Obsoletes: kde5-video-player-0-dummy < %EVR
#
Provides: kde-video-player = %EVR
Provides: kde-video-player-dummy = %EVR
Requires: kde-common
%description -n kde-video-player-0-dummy
%summary

%package -n kde-video-player-2-dragon
Group: Graphical desktop/KDE
Summary: Dragon video player
Provides: kde5-video-player-2-dragon = %EVR
Obsoletes: kde5-video-player-2-dragon < %EVR
#
Provides: kde-video-player = %EVR
Provides: kde-video-player-dragon = %EVR
Requires: kde-common
Requires: kde5-dragon
%description -n kde-video-player-2-dragon
%summary

%package -n kde-video-player-3-kaffeine
Group: Graphical desktop/KDE
Summary: Kaffeine video player
Provides: kde5-video-player-3-kaffeine = %EVR
Obsoletes: kde5-video-player-3-kaffeine < %EVR
#
Provides: kde-video-player = %EVR
Provides: kde-video-player-kaffeine = %EVR
Requires: kde-common
Requires: kde5-kaffeine
%description -n kde-video-player-3-kaffeine
%summary

%package -n kde-video-player-4-smplayer
Group: Graphical desktop/KDE
Summary: SMplayer video player
Provides: kde5-video-player-4-smplayer = %EVR
Obsoletes: kde5-video-player-4-smplayer < %EVR
#
Provides: kde-video-player = %EVR
Provides: kde-video-player-smplayer = %EVR
Requires: kde-common
Requires: kde5-smplayer
%description -n kde-video-player-4-smplayer
%summary

%package -n kde-video-player-5-haruna
Group: Graphical desktop/KDE
Summary: Haruna video player
Provides: kde5-video-player-5-haruna = %EVR
Obsoletes: kde5-video-player-5-haruna < %EVR
#
Provides: kde-video-player = %EVR
Provides: kde-video-player-haruna = %EVR
Requires: kde-common
Requires: kde5-haruna
%description -n kde-video-player-5-haruna
%summary

%package -n kde-volume-control-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy volume control
Provides: kde5-volume-control-0-dummy = %EVR
Obsoletes: kde5-volume-control-0-dummy < %EVR
#
Provides: kde-volume-control = %EVR
Provides: kde-volume-control-dummy = %EVR
Requires: kde-common
%description -n kde-volume-control-0-dummy
%summary

%package -n kde-volume-control-2-alsa
Group: Graphical desktop/KDE
Summary: KMix volume control
Provides: kde5-volume-control-2-alsa = %EVR
Obsoletes: kde5-volume-control-2-alsa < %EVR
#
Provides: kde-volume-control = %EVR
Provides: kde-volume-control-kmix = %EVR
Requires: kde-common
Requires: kde5-kmix
%description -n kde-volume-control-2-alsa
%summary

%package -n kde-volume-control-6-pulseaudio
Group: Graphical desktop/KDE
Summary: PulseAudio volume control
Provides: kde5-volume-control-6-pulseaudio = %EVR
Obsoletes: kde5-volume-control-6-pulseaudio < %EVR
#
Provides: kde-volume-control = %EVR
Provides: kde-volume-control-pulseaudio = %EVR
Requires: kde-common
Requires: plasma-pa
Requires: pulseaudio-daemon
%description -n kde-volume-control-6-pulseaudio
%summary

%package -n kde-volume-control-7-pipewire
Group: Graphical desktop/KDE
Summary: PipeWire volume control
Provides: kde5-volume-control-7-pipewire = %EVR
Obsoletes: kde5-volume-control-7-pipewire < %EVR
#
Provides: kde-volume-control = %EVR
Provides: kde-volume-control-pipewire = %EVR
Requires: kde-common
Requires: plasma-pa
Requires: pipewire pipewire-utils wireplumber
#
Provides: kde5-volume-control-4-pipewire = %EVR
Obsoletes: kde5-volume-control-4-pipewire < %EVR
%description -n kde-volume-control-7-pipewire
%summary

%package -n kde-email-client-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy email client
Provides: kde5-email-client-0-dummy = %EVR
Obsoletes: kde5-email-client-0-dummy < %EVR
#
Provides: kde-email-client = %EVR
Provides: kde-email-client-dummy = %EVR
Requires: kde-common
%description -n kde-email-client-0-dummy
%summary

%package -n kde-email-client-2-kmail
Group: Graphical desktop/KDE
Summary: KMail email client
Provides: kde5-email-client-2-kmail = %EVR
Obsoletes: kde5-email-client-2-kmail < %EVR
#
Provides: kde-email-client = %EVR
Provides: kde-email-client-kmail = %EVR
Requires: kde-common
Requires: kde5-kmail kde5-pim-addons-kmail kde5-pim-addons-plugins bogofilter bogofilter-utils
Requires: kde5-akonadi-import-wizard kde5-kmail-account-wizard kde5-mbox-importer kde5-pim-sieve-editor
Requires: kde5-grantlee-editor
%description -n kde-email-client-2-kmail
%summary

%package -n kde-email-client-4-thunderbird
Group: Graphical desktop/KDE
Summary: Thunderbird email client
Provides: kde5-email-client-4-thunderbird = %EVR
Obsoletes: kde5-email-client-4-thunderbird < %EVR
#
Provides: kde-email-client = %EVR
Provides: kde-email-client-thunderbird = %EVR
Requires: kde-common
Requires: thunderbird thunderbird-ru thunderbird-lightning-ru
%description -n kde-email-client-4-thunderbird
%summary

%package -n kde-audio-player-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy audio player
Provides: kde5-audio-player-0-dummy = %EVR
Obsoletes: kde5-audio-player-0-dummy < %EVR
#
Provides: kde-audio-player = %EVR
Provides: kde-audio-player-dummy = %EVR
Requires: kde-common
%description -n kde-audio-player-0-dummy
%summary

%package -n kde-audio-player-2-elisa
Group: Graphical desktop/KDE
Summary: Elisa audio player
Provides: kde5-audio-player-2-elisa = %EVR
Obsoletes: kde5-audio-player-2-elisa < %EVR
#
Provides: kde-audio-player = %EVR
Provides: kde-audio-player-elisa = %EVR
Requires: kde-common
Requires: kde5-elisa
%description -n kde-audio-player-2-elisa
%summary

%package -n kde-audio-player-4-qmmp
Group: Graphical desktop/KDE
Summary: QMMP audio player
Provides: kde5-audio-player-4-qmmp = %EVR
Obsoletes: kde5-audio-player-4-qmmp < %EVR
#
Provides: kde-audio-player = %EVR
Provides: kde-audio-player-qmmp = %EVR
Requires: kde-common
Requires: qmmp
%description -n kde-audio-player-4-qmmp
%summary

%package -n kde-messenger-client-0-dummy
Group: Graphical desktop/KDE
Summary: Dummy messaging client
Provides: kde5-messenger-client-0-dummy = %EVR
Obsoletes: kde5-messenger-client-0-dummy < %EVR
#
Provides: kde-messenger-client = %EVR
Provides: kde-messenger-client-dummy = %EVR
Requires: kde-common
%description -n kde-messenger-client-0-dummy
%summary

%package -n kde-messenger-client-6-mix
Group: Graphical desktop/KDE
Summary: Mixed messaging client
Provides: kde5-messenger-client-6-mix = %EVR
Obsoletes: kde5-messenger-client-6-mix < %EVR
#
Provides: kde-messenger-client = %EVR
Provides: kde-messenger-client-mix = %EVR
Requires: kde-common
#Requires: choqok
#Requires: jami
#Requires: kde5-konversation
%ifnarch armh ppc64le aarch64
#Requires: telegram-desktop
%endif
Requires: psi-plus psi-plus-l10n psi-plus-plugin-autoreply psi-plus-plugin-cleaner psi-plus-plugin-conferencelogger psi-plus-plugin-contentdownloader
Requires: psi-plus-plugin-enummessages psi-plus-plugin-historykeeper psi-plus-plugin-image psi-plus-plugin-imagepreview psi-plus-plugin-messagefilter
Requires: psi-plus-plugin-otr psi-plus-plugin-stopspam psi-plus-plugin-storagenotes
%description -n kde-messenger-client-6-mix
%summary

%package -n kde-display-manager-0-dummy
Group: Graphical desktop/KDE
Summary:  Dummy Display Manager collective package
Provides: kde5-display-manager-0-dummy = %EVR
Obsoletes: kde5-display-manager-0-dummy < %EVR
#
Provides: kde-display-manager = %EVR
Provides: kde-display-manager-dummy = %EVR
Requires: kde-common
%description -n kde-display-manager-0-dummy
%summary

%package -n kde-display-manager-5-sddm
Group: Graphical desktop/KDE
Summary: SDDM Display Manager collective package
Provides: kde5-display-manager-5-sddm = %EVR
Obsoletes: kde5-display-manager-5-sddm < %EVR
#
Provides: kde-display-manager = %EVR
Provides: kde-display-manager-sddm = %EVR
Requires: kde-common
Requires: sddm sddm-theme-breeze sddm-kcm dm-tool
%description -n kde-display-manager-5-sddm
%summary

%package -n kde-display-manager-6-lightdmgtk
Group: Graphical desktop/KDE
Summary:  LightDM Display Manager collective package
Provides: kde5-display-manager-6-lightdmgtk = %EVR
Obsoletes: kde5-display-manager-6-lightdmgtk < %EVR
#
Provides: kde-display-manager = %EVR
Provides: kde-display-manager-lightdmgtk = %EVR
Requires: kde-common
Requires: lightdm-gtk-greeter lightdm-gtk-greeter-settings dm-tool
%description -n kde-display-manager-6-lightdmgtk
%summary

%package -n kde-display-manager-7-lightdm
Group: Graphical desktop/KDE
Summary:  LightDM Display Manager collective package
Provides: kde5-display-manager-7-lightdm = %EVR
Obsoletes: kde5-display-manager-7-lightdm < %EVR
#
Provides: kde-display-manager = %EVR
Provides: kde-display-manager-lightdm = %EVR
Requires: kde-common
Requires: lightdm-kde-greeter dm-tool
%description -n kde-display-manager-7-lightdm
%summary

%files -n kde-network-manager-0-dummy
%files -n kde-network-manager-2-etcnet
%files -n kde-network-manager-4-nm

%files -n kde-video-player-0-dummy
%files -n kde-video-player-2-dragon
%files -n kde-video-player-3-kaffeine
%files -n kde-video-player-4-smplayer
%files -n kde-video-player-5-haruna

%files -n kde-volume-control-0-dummy
%files -n kde-volume-control-2-alsa
%files -n kde-volume-control-6-pulseaudio
%files -n kde-volume-control-7-pipewire

%files -n kde-email-client-0-dummy
%if_enabled qtwebengine
%files -n kde-email-client-2-kmail
%endif
%ifnarch armh
%files -n kde-email-client-4-thunderbird
%endif

%files -n kde-audio-player-0-dummy
%files -n kde-audio-player-2-elisa
%files -n kde-audio-player-4-qmmp

%files -n kde-messenger-client-0-dummy
%files -n kde-messenger-client-6-mix

%files -n kde-display-manager-0-dummy
%files -n kde-display-manager-5-sddm
%files -n kde-display-manager-6-lightdmgtk
%files -n kde-display-manager-7-lightdm

%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt1
- fix provides

* Fri Jul 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt1
- clear requires

* Thu Jul 18 2024 Sergey V Turchin <zerg@altlinux.org> 6.0.0-alt1
- initial build
