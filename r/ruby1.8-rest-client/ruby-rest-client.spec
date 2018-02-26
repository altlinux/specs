%define ruby_major 1.8
%define orig_name rest-client

Summary: Simple REST client for Ruby
Name: ruby%ruby_major-%orig_name
Version: 1.6.6
Release: alt1
Group: Development/Ruby
License: MIT
URL: http://github.com/archiloque/rest-client
Source0: %orig_name-%version.tar
Patch0: %orig_name-%version-%release.patch

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby%ruby_major-rake
BuildRequires: ruby%ruby_major-tool-setup

%description
A simple Simple HTTP and REST client for Ruby, inspired by the Sinatra
microframework style of specifying actions: get, put, post, delete.


%prep
%setup -q -n %orig_name-%version
%patch -p1
%update_setup_rb

%build
%ruby_config

%install
mkdir -p %buildroot
%ruby_install


%files
%_bindir/restclient
%ruby_sitelibdir/*


%changelog
* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Initial ruby-1.8 version build for Sisyphus

