%define _unpackaged_files_terminate_build 1

%def_with check

Name: pgadmin3
Version: 1.27.0
Release: alt1

Summary: Graphical administration and development tool for PostgreSQL
License: PostgreSQL
Group: Databases
Url: https://github.com/levinsv/pgadmin3
Vcs: https://github.com/levinsv/pgadmin3.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: libwxGTK3.2-devel
BuildRequires: libpq5-18-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libcurl-devel
%if_with check
BuildRequires: catch2-devel
BuildRequires: ctest
%endif

%description
pgAdmin III is a graphical administration and development tool for
PostgreSQL. This maintained fork supports modern PostgreSQL versions,
including PostgreSQL 18, and extends the SQL editor, query results,
server monitoring and database object management tools.

%prep
%setup -q
# Do not strip the executable: RPM produces debuginfo itself.
# Register Linux tests at the top CMake level, as validated with hasher.
sed -i \
    -e '/^add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD/,/^)[[:space:]]*$/d' \
    -e '/^[[:space:]]*set(RPATH "\.")[[:space:]]*$/d' \
    -e '/^[[:space:]]*list(APPEND CMAKE_BUILD_RPATH ${RPATH})[[:space:]]*$/d' \
    -e '/^[[:space:]]*add_subdirectory(tests)[[:space:]]*$/d' \
    CMakeLists.txt

%if_with check
cat >> CMakeLists.txt <<'EOF_CMAKE'

enable_testing()
add_subdirectory(tests)
EOF_CMAKE
%endif

%build
%cmake
%if_with check
# Fail early if CMake silently skips the tests.
test -f %_cmake__builddir/CTestTestfile.cmake
test -f %_cmake__builddir/tests/CTestTestfile.cmake
%endif

%cmake_build

%install
# Upstream currently has no install(TARGETS ...) rule.
install -Dpm0755 %_cmake__builddir/pgadmin3 \
    %buildroot%_bindir/pgadmin3

# Prefer the largest upstream application icon, if supplied.
for icon in include/images/pgAdmin3.png \
            include/images/pgAdmin3-32.png \
            include/images/pgAdmin3-16.png; do
    if test -f "$icon"; then
        install -Dpm0644 "$icon" \
            %buildroot%_datadir/pixmaps/pgadmin3.png
        break
    fi
done
test -f %buildroot%_datadir/pixmaps/pgadmin3.png || {
    echo 'ERROR: pgAdmin III application icon was not found' >&2
    exit 1
}

install -d -m0755 %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/pgadmin3.desktop <<'EOF_DESKTOP'
[Desktop Entry]
Type=Application
Name=pgAdmin III
Comment=PostgreSQL administration and development
Comment[ru]=Администрирование и разработка для PostgreSQL
Exec=pgadmin3
Icon=pgadmin3
Terminal=false
StartupNotify=true
Categories=Development;Database;
Keywords=PostgreSQL;Database;SQL;
EOF_DESKTOP

%check
ctest --test-dir %_cmake__builddir \
    --output-on-failure --no-tests=error

%files
%doc README.md INSTALL.txt INSTALL_EN.txt changelog.md LICENSE
%_bindir/pgadmin3
%_datadir/applications/pgadmin3.desktop
%_datadir/pixmaps/pgadmin3.png

%changelog
* Tue Oct 20 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.27.0-alt1
- Initial build for ALT Sisyphus (Closes: #60633).
