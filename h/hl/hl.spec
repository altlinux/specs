Name: hl
Version: 1.93
Release: alt1

Summary: Command-line text colorization tool using regular expressions
License: GPL-3.0-or-later
Group: Text tools
Url: https://github.com/mbornet-hl/hl

# Source-url: https://github.com/mbornet-hl/hl/archive/refs/heads/master.tar.gz
Source: %name-%version.tar
Patch: %name-default-config-path.patch

BuildRequires: flex

%description
hl can greatly help you read log files, the output of commands or scripts,
configuration files, text files. It can highlight thresholds, colorize blocks
of text delimited by markers, alternate colors when the value of an element
changes (or on the contrary when it does not change), check values consistency
on a line, colorize fields of text, and so on. Many configurations have been
created, and you can easily create yours to suit your needs, using simple text
strings or regular expressions.

Its purpose is to colorize what is important in the text you read. It has been
designed to help you get straight to the point. It's fast and efficient.

%prep
%setup
%patch -p1

%build
%make_build

%install
install -Dpm 0755 hl %buildroot%_bindir/hl
install -Dpm 0644 man1/hl.1 %buildroot%_man1dir/hl.1
install -Dpm 0644 man5/hl.5 %buildroot%_man5dir/hl.5

# Install configuration files
mkdir -p %buildroot%_datadir/%name/configs
install -pm 0644 config_files/*.cfg %buildroot%_datadir/%name/configs/

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/%name.5*
%_datadir/%name/

%changelog
* Tue Jan 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.93-alt1
- initial build for ALT Sisyphus (snapshot from master branch)
- add /usr/share/hl/configs to default config search path
