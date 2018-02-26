Name: asterisk-sounds-base
Summary: sounds for Asterisk
Version: 0.1
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
%define sound_dir	%_datadir/asterisk/sounds/
Requires(pre): asterisk-base >= 0.6

%package -n asterisk-sounds-en-base
Summary: sounds for Asterisk
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-base >= %version-%release

%description -n asterisk-sounds-en-base
sounds for Asterisk

%package -n asterisk-sounds-en_AU-base
Summary: sounds for Asterisk
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-base >= %version-%release

%description -n asterisk-sounds-en_AU-base
sounds for Asterisk

%package -n asterisk-sounds-es-base
Summary: sounds for Asterisk
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-base >= %version-%release

%description -n asterisk-sounds-es-base
sounds for Asterisk

%package -n asterisk-sounds-fr-base
Summary: sounds for Asterisk
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-base >= %version-%release

%description -n asterisk-sounds-fr-base
sounds for Asterisk

%package -n asterisk-sounds-ru-base
Summary: sounds for Asterisk
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-sounds-base >= %version-%release

%description -n asterisk-sounds-ru-base
sounds for Asterisk

%description
sounds for Asterisk


%install
mkdir -p %buildroot%sound_dir/{en,en_AU,ru,fr,es}

%files

%files -n asterisk-sounds-en-base
%dir %sound_dir/en

%files -n asterisk-sounds-en_AU-base
%dir %sound_dir/en_AU

%files -n asterisk-sounds-es-base
%dir %sound_dir/es

%files -n asterisk-sounds-fr-base
%dir %sound_dir/fr

%files -n asterisk-sounds-ru-base
%dir %sound_dir/ru

%changelog
* Sun Jul 24 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

