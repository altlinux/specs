%define _unpackaged_files_terminate_build 1

%define pluginsdir %_datadir/zsh/plugins
%define zsh_minimum_version 4.3.11

Name: zsh-autosuggestions
Version: 0.7.1
Release: alt1

Summary: Fish-like autosuggestions for zsh
License: MIT
Group: Development/Tools
Url: https://github.com/zsh-users/zsh-autosuggestions
Vcs: https://github.com/zsh-users/zsh-autosuggestions.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: zsh >= %zsh_minimum_version

BuildRequires(pre): rpm-macros-make

%description
Fish-like fast/unobtrusive autosuggestions for zsh.

It suggests commands as you type based on history and completions.

Contains update, test and create commands.

Plugin placed under %pluginsdir/%name

%prep
%setup
%autopatch -p1

%install
install -vpDm 644 %name.zsh -t %buildroot/%pluginsdir/%name
install -vpDm 644 %name.plugin.zsh -t %buildroot/%pluginsdir/%name

%files
%pluginsdir/%name/
%doc CHANGELOG.md README.md

%changelog
* Mon Feb 17 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.7.1-alt1
- Initial build.
