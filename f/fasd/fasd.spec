Name: 	  fasd
Version:  1.0.1.0.7.git90b531a
Release:  alt1

Summary:  Command-line productivity booster, offers quick access to files and directories

License:  MIT
Group:    Other
Url: 	  https://github.com/clvv/fasd.git

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch0:   fasd-1.0.1.0.7.git90b531a-fix_shebang.patch

BuildArch: noarch

%description
Fasd (pronounced similar to "fast") is a command-line productivity booster.
Fasd offers quick access to files and directories for POSIX shells.
It is inspired by tools like autojump, z and v. Fasd keeps track of files
and directories you have accessed, so that you can quickly reference them
in the command line.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 16 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.1.0.7.git90b531a-alt1
- Initial build for Sisyphus.
