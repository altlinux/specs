%define        gemname ruby_gntp

Name:          gem-ruby-gntp
Version:       0.3.4
Release:       alt1
Summary:       Ruby library for GNTP(Growl Notification Transport Protocol) client
License:       MIT
Group:         Development/Ruby
Url:           http://snaka.github.com/ruby_gntp/
Vcs:           https://github.com/snaka/ruby_gntp.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ruby_gntp) = 0.3.4

%description
Ruby library for GNTP(Growl Notification Transport Protocol) client.


%package       -n gem-ruby-gntp-doc
Version:       0.3.4
Release:       alt1
Summary:       Ruby library for GNTP(Growl Notification Transport Protocol) client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_gntp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_gntp) = 0.3.4

%description   -n gem-ruby-gntp-doc
Ruby library for GNTP(Growl Notification Transport Protocol) client
documentation files.

%description   -n gem-ruby-gntp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_gntp.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ruby-gntp-doc
%doc README
%ruby_gemdocdir


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.4-alt1
- + packaged gem with Ruby Policy 2.0
