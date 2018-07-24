%define orig_name rest-client

Summary: Simple REST client for Ruby
Name: ruby-%orig_name
Version: 2.0.2
Release: alt1
Group: Development/Ruby
License: MIT
URL: http://github.com/archiloque/rest-client
Source0: %orig_name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-rake
BuildRequires: ruby-tool-setup

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.

%prep
%setup -q -n %orig_name-%version
%update_setup_rb

%build
%ruby_config

%install
mkdir -p %buildroot
%ruby_install

%files
%doc AUTHORS README*
%_bindir/restclient
%ruby_sitelibdir/*
%rubygem_specdir/*

%changelog
* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.6.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- cleaned up BuildRequires

* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Initial build for Sisyphus

