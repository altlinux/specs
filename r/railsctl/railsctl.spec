Name:          railsctl
Version:       1.0.2
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
* Mon Feb 03 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- * changed bunlde function to apply install with test,dev first before update

* Wed Jan 15 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + added GEM_HOME for proper run of rails
- - disabled apipie, and encryption

* Mon Aug 19 2024 Pavel Skrylev <majioa@altlinux.org> 1.0-alt1
- initial build for Sisyphus
