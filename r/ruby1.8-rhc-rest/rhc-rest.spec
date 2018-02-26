%define ruby_major 1.8
%define orig_name rhc-rest

Summary:       Ruby bindings/client for OpenShift REST API
Name:          ruby%ruby_major-%orig_name
Version:       0.0.11
Release:       alt1
Group:         System/Servers
License:       ASL 2.0
URL:           http://openshift.redhat.com
Source0:       %orig_name-%version.tar
Patch0:        %orig_name-%version-%release.patch

BuildArch:     noarch

BuildRequires: rpm-build-ruby ruby%ruby_major-rake
BuildRequires: ruby%ruby_major-tool-setup

%description
Provides Ruby bindings/client for OpenShift REST API

%prep
%setup -n %orig_name-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc LICENSE COPYRIGHT
%ruby_sitelibdir/*

%changelog
* Sat Apr 14 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.11-alt1
- Initial ruby-1.8 version build for Sisyphus

