Summary:	MS compress/expand-compatible (de)compressor
Summary(pl.UTF-8):	(De)kompresor zgodny z MS compress/expand
Name:		mscompress
Version:	0.4
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	https://github.com/stapelberg/mscompress/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3196bcdb3e3ac4e68a55c165c3055e83
URL:		https://github.com/stapelberg/mscompress
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microsoft compress.exe/expand.exe-compatible file (de)compressor.

%description -l pl.UTF-8
Program kompresujący i dekompresujący zgodny z compress.exe/expand.exe
Microsoftu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO format.txt
%attr(755,root,root) %{_bindir}/mscompress
%attr(755,root,root) %{_bindir}/msexpand
%{_mandir}/man1/mscompress.1*
%{_mandir}/man1/msexpand.1*
