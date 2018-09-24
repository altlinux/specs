%define  pkgname concurrent-ruby

Name:    ruby-%pkgname
Version: 1.0.5
Release: alt2

Summary: Modern concurrency tools including agents, futures, promises, thread pools, supervisors, and more.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/ruby-concurrency/concurrent-ruby

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%package edge
Summary: Edge features and additions to the concurrent-ruby gem
Group: Development/Ruby

BuildArch: noarch

%description edge
These features are under active development and may change frequently. They are
expected not to keep backward compatibility (there may also lack tests and
documentation). Semantic versions will be obeyed though. Features developed in
`concurrent-ruby-edge` are expected to move to `concurrent-ruby` when final.
Please see http://concurrent-ruby.com for more information.

%package edge-doc
Summary: Documentation files for %name-edge
Group: Documentation

BuildArch: noarch

%description edge-doc
Documentation files for %{name}-edge.

%package ext
Summary: C extensions to optimize concurrent-ruby under MRI
Group: Development/Ruby

%description ext
C extensions to optimize the concurrent-ruby gem when running under MRI.
Please see http://concurrent-ruby.com for more information.


%prep
%setup -n %pkgname-%version
rm -f Gemfile
mkdir -p %{name}-ext %{name}-edge
mv *ext.gemspec %{name}-ext
mv *edge.gemspec %{name}-edge
ln -s ../lib %{name}-edge/lib
ln -s ../support/file_map.rb %{name}-edge/lib/file_map.rb
ln -s ../lib %{name}-ext/lib

for dir in . %{name}-ext %{name}-edge ;do
   pushd $dir
   %update_setup_rb
   popd
done

%build
for dir in . %{name}-ext %{name}-edge ;do
   pushd $dir
   %ruby_config
   %ruby_build
   popd
done

%install
for dir in . %{name}-ext %{name}-edge ;do
   pushd $dir
   echo 1111
   pwd
   ls
   %ruby_install
   ls -la
   popd
done
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README* CHANGELOG*
%ruby_sitelibdir/concurrent*
%exclude %ruby_sitelibdir/concurrent-edge.rb
%exclude %ruby_sitelibdir/concurrent/actor*
%exclude %ruby_sitelibdir/concurrent/channel*
%exclude %ruby_sitelibdir/concurrent/edge*
%exclude %ruby_sitelibdir/concurrent/lazy_register.rb
%rubygem_specdir/%{pkgname}*

%files doc
%ruby_ri_sitedir/lib/concurrent/thread_safe/page-readme_txt.ri
%ruby_ri_sitedir/Concurrent*
%exclude %ruby_ri_sitedir/Concurrent/Actor*
%exclude %ruby_ri_sitedir/Concurrent/Channel*
%exclude %ruby_ri_sitedir/Concurrent/Edge*

%files edge
%ruby_sitelibdir/concurrent-edge.rb
%ruby_sitelibdir/concurrent/actor*
%ruby_sitelibdir/concurrent/channel*
%ruby_sitelibdir/concurrent/edge*
%ruby_sitelibdir/concurrent/lazy_register.rb
%rubygem_specdir/%{name}-edge*

%files edge-doc
%ruby_ri_sitedir/Concurrent/Actor*
%ruby_ri_sitedir/Concurrent/Channel*
%ruby_ri_sitedir/Concurrent/Edge*

%files ext
%ruby_sitearchdir/concurrent/extension.so
%rubygem_specdir/%{name}-ext*

%changelog
* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2
- Gemify build for Sisyphus

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
