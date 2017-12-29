%global gem_name activerecord
%global gem_dir /usr/lib/ruby/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%global gem_instdir %gem_dir/gems
%global gem_docdir %gem_dir/doc
%global gem_cache %gem_dir/cache

Name: activerecord-gems
Version: 5.0.2
Release: alt2
Summary: ActiveRecord
Group: Development/Ruby
License: MIT,Apache2.0
Url: http://rubygems.org
packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar
BuildRequires: ruby  ruby-tools libruby-devel 
BuildRequires: activesupport-gems
BuildArch: noarch
Obsoletes: ruby-activerecord < 5.0.2

%description
ActiveRecord ruby gem


%package doc
Summary: Documentation for %name
Group: Documentation
# SyntaxHighlighter is dual licensed under the MIT and GPL licenses
License: MIT and (MIT or GPL+)
BuildArch: noarch

%description doc
Documentation for %name.

%prep
%setup -c -T
tar xvf %SOURCE0
%build
%install
cd %name-%version
#gem install --user builder*.gem
#gem install --user rack*.gem
#gem install --user erubis*.gem
#gem install --user nokogiri*.gem
#gem install --user loo*.gem
#gem install --user thor*.gem
#gem install --user mini_portile*.gem
gem install --user --local activemodel*.gem
gem install --user --local arel*.gem
gem install --user --local active*.gem
#gem install --user --local rails-dom-testing*.gem
#gem install --user rails-html*.gem
#gem install --user railties*.gem
#gem install --user sprockets-3*.gem
#gem install --user *.gem
cd ~/.gem/ruby/%(%ruby_rubyconf RUBY_LIB_VERSION)
tar czvf ~/ar.tgz *

mkdir -p %buildroot/%gem_dir 
cd %buildroot/%gem_dir 
%add_findreq_skiplist /usr/lib/ruby/gems/*

tar xzvf ~/ar.tgz
rm -f gems/thread_safe-0.3.6/examples/bench_cache.rb
# this file has bad shebang 
%files
%gem_dir/*
%exclude %gem_cache
%exclude %gem_docdir


%files doc
%doc %gem_docdir

%changelog
* Sun Nov 12 2017 Denis Medvedev <nbr@altlinux.org> 5.0.2-alt2
- Fixed gem dir. Added needed obsoletes.

* Mon Mar 20 2017 Denis Medvedev <nbr@altlinux.org> 5.0.2-alt1
- initial build for ALT Linux Sisyphus. Based on gems.
