%define _unpackaged_files_terminate_build 1
# Busted not in sisyphus yet.
%def_without check
%define luarocks_revision 0

Name: lua5.4-module-mediator_lua
Version: 1.1.2
Release: alt1_lr%luarocks_revision

Summary: Mediator pattern implementation for pub-sub management
License: MIT
Group: Development/Other
Url: https://olivinelabs.com/mediator_lua/
Vcs: https://github.com/Olivine-Labs/mediator_lua
BuildArch: noarch

Source: %name-%version.tar

Provides: luarocks5.4(mediator_lua) = %EVR

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks

%description
Mediator_lua is a simple class that allows you to listen to events by
subscribing to and sending data to channels. Its purpose is to help you
decouple code where you might otherwise have functions calling
functions calling functions, and instead simply call
mediator.publish("chat", { message = "hi" })

%prep
%setup

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	mediator_lua-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
luarocks-5.4 test --test-type busted mediator_lua-%version-%luarocks_revision.rockspec

%files
%luarocks_dbdir/mediator_lua
%lua_modulesdir_noarch/mediator.lua

%changelog
* Tue Apr 08 2025 Sergey Zhidkih <rx1513@altlinux.org> 1.1.2-alt1_lr0
- First build for alt.
