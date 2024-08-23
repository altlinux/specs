Name:          railsctl
Version:       1.0
Release:       alt1
Summary:       Ruby-on-Rails control script
License:       MIT
Group:         Development/Ruby
BuildArch:     noarch

Source:        %name-%version.tar

%description
Ruby-on-Rails control script allowing to setup or run rails application like
Foreman on-the-fly using system's ruby.


%prep
%setup

%install
install -D -m 755 %name %buildroot%_sbindir/%name

%files
%_sbindir/railsctl


%changelog
* Mon Aug 19 2024 Pavel Skrylev <majioa@altlinux.org> 1.0-alt1
- initial build for Sisyphus
