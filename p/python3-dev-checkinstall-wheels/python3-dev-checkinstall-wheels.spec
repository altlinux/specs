%define _unpackaged_files_terminate_build 1

%global submajor 14
%global tool_dir %_datadir/python3.%{submajor}/Tools


Name: python3-dev-checkinstall-wheels
Version: 3.%submajor
Release: alt1

Summary: Special package with tests and wheels for python3-dev-checkinstall

License: GPLv3
Group: Development/Python3

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot/%tool_dir/wheels_for_checkinstall-%version
file_list='meson-*-py3-none-any.whl
           packaging-*-py3-none-any.whl
           pyxcrypt-*.tar.gz
           meson_python-*-py3-none-any.whl
           pyproject_metadata-*-py3-none-any.whl'

for file in $file_list
do
    install $file %buildroot/%tool_dir/wheels_for_checkinstall-%version
done

%files
%tool_dir/wheels_for_checkinstall-%version

%changelog
* Wed May 06 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 3.14-alt1
- Initial release for Sisyphus
