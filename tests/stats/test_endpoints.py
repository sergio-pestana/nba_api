from nba_api.stats.endpoints import *

test = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoreadvancedv2')
test = boxscorefourfactorsv2.BoxScoreFourFactorsV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscorefourfactorsv2')
test = boxscoremiscv2.BoxScoreMiscV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoremiscv2')
test = boxscoreplayertrackv2.BoxScorePlayerTrackV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoreplayertrackv2')
test = boxscorescoringv2.BoxScoreScoringV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscorescoringv2')
test = boxscoresummaryv2.BoxScoreSummaryV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoresummaryv2')
test = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoretraditionalv2')
test = boxscoreusagev2.BoxScoreUsageV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'boxscoreusagev2')
test = commonallplayers.CommonAllPlayers().nba_response.valid_json()
if not test:
    raise Exception('fail', 'commonallplayers')
test = commonplayerinfo.CommonPlayerInfo(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'commonplayerinfo')
test = commonplayoffseries.CommonPlayoffSeries().nba_response.valid_json()
if not test:
    raise Exception('fail', 'commonplayoffseries')
test = commonteamroster.CommonTeamRoster(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'commonteamroster')
test = commonteamyears.CommonTeamYears().nba_response.valid_json()
if not test:
    raise Exception('fail', 'commonteamyears')
test = defensehub.DefenseHub(season='2017-18').nba_response.valid_json()
if not test:
    raise Exception('fail', 'defensehub')
test = draftcombinedrillresults.DraftCombineDrillResults().nba_response.valid_json()
if not test:
    raise Exception('fail', 'draftcombinedrillresults')
test = draftcombinenonstationaryshooting.DraftCombineNonStationaryShooting().nba_response.valid_json()
if not test:
    raise Exception('fail', 'draftcombinenonstationaryshooting')
test = draftcombineplayeranthro.DraftCombinePlayerAnthro().nba_response.valid_json()
if not test:
    raise Exception('fail', 'draftcombineplayeranthro')
test = draftcombinespotshooting.DraftCombineSpotShooting().nba_response.valid_json()
if not test:
    raise Exception('fail', 'draftcombinespotshooting')
test = draftcombinestats.DraftCombineStats().nba_response.valid_json()
if not test:
    raise Exception('fail', 'draftcombinestats')
test = drafthistory.DraftHistory().nba_response.valid_json()
if not test:
    raise Exception('fail', 'drafthistory')
test = franchisehistory.FranchiseHistory().nba_response.valid_json()
if not test:
    raise Exception('fail', 'franchisehistory')
test = homepageleaders.HomePageLeaders().nba_response.valid_json()
if not test:
    raise Exception('fail', 'homepageleaders')
test = homepagev2.HomePageV2().nba_response.valid_json()
if not test:
    raise Exception('fail', 'homepagev2')
test = infographicfanduelplayer.InfographicFanDuelPlayer(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'infographicfanduelplayer')
test = leaderstiles.LeadersTiles().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaderstiles')
test = leaguedashlineups.LeagueDashLineups().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashlineups')
test = leaguedashplayerbiostats.LeagueDashPlayerBioStats().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashplayerbiostats')
test = leaguedashplayerclutch.LeagueDashPlayerClutch().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashplayerclutch')
test = leaguedashplayerptshot.LeagueDashPlayerPtShot().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashplayerptshot')
test = leaguedashplayershotlocations.LeagueDashPlayerShotLocations().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashplayershotlocations')
test = leaguedashplayerstats.LeagueDashPlayerStats().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashplayerstats')
test = leaguedashptdefend.LeagueDashPtDefend().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashptdefend')
test = leaguedashptstats.LeagueDashPtStats().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashptstats')
test = leaguedashptteamdefend.LeagueDashPtTeamDefend().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashptteamdefend')
test = leaguedashteamclutch.LeagueDashTeamClutch().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashteamclutch')
test = leaguedashteamptshot.LeagueDashTeamPtShot().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashteamptshot')
test = leaguedashteamshotlocations.LeagueDashTeamShotLocations().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashteamshotlocations')
test = leaguedashteamstats.LeagueDashTeamStats().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguedashteamstats')
test = leaguegamefinder.LeagueGameFinder().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguegamefinder')
test = leaguegamelog.LeagueGameLog().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguegamelog')
test = leagueleaders.LeagueLeaders().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leagueleaders')
test = leaguestandings.LeagueStandings().nba_response.valid_json()
if not test:
    raise Exception('fail', 'leaguestandings')
test = playbyplay.PlayByPlay(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playbyplay')
test = playbyplayv2.PlayByPlayV2(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playbyplayv2')
test = playerawards.PlayerAwards(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerawards')
test = playercareerstats.PlayerCareerStats(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playercareerstats')
test = playercompare.PlayerCompare(player_id_list='202681,203078,2544,201567,203954',
                                   vs_player_id_list='201566,201939,201935,201142,203076').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playercompare')
test = playerdashptpass.PlayerDashPtPass(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashptpass')
test = playerdashptreb.PlayerDashPtReb(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashptreb')
test = playerdashptshotdefend.PlayerDashPtShotDefend(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashptshotdefend')
test = playerdashptshots.PlayerDashPtShots(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashptshots')
test = playerdashboardbyclutch.PlayerDashboardByClutch(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbyclutch')
test = playerdashboardbygamesplits.PlayerDashboardByGameSplits(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbygamesplits')
test = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbygeneralsplits')
test = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbylastngames')
test = playerdashboardbyopponent.PlayerDashboardByOpponent(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbyopponent')
test = playerdashboardbyshootingsplits.PlayerDashboardByShootingSplits(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbyshootingsplits')
test = playerdashboardbyteamperformance.PlayerDashboardByTeamPerformance(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbyteamperformance')
test = playerdashboardbyyearoveryear.PlayerDashboardByYearOverYear(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerdashboardbyyearoveryear')
test = playerfantasyprofile.PlayerFantasyProfile(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerfantasyprofile')
test = playerfantasyprofilebargraph.PlayerFantasyProfileBarGraph(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerfantasyprofilebargraph')
test = playergamelog.PlayerGameLog(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playergamelog')
test = playergamestreakfinder.PlayerGameStreakFinder().nba_response.valid_json()
if not test:
    raise Exception('fail', 'playergamestreakfinder')
test = playernextngames.PlayerNextNGames(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playernextngames')
test = playerprofilev2.PlayerProfileV2(player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playerprofilev2')
test = playervsplayer.PlayerVsPlayer(player_id='2544', vs_player_id='202681').nba_response.valid_json()
if not test:
    raise Exception('fail', 'playervsplayer')
test = playoffpicture.PlayoffPicture().nba_response.valid_json()
if not test:
    raise Exception('fail', 'playoffpicture')
test = scoreboard.Scoreboard().nba_response.valid_json()
if not test:
    raise Exception('fail', 'scoreboard')
test = scoreboardv2.ScoreboardV2().nba_response.valid_json()
if not test:
    raise Exception('fail', 'scoreboardv2')
test = shotchartdetail.ShotChartDetail(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'shotchartdetail')
test = shotchartlineupdetail.ShotChartLineupDetail().nba_response.valid_json()
if not test:
    raise Exception('fail', 'shotchartlineupdetail')
test = teamdashlineups.TeamDashLineups(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashlineups')
test = teamdashptpass.TeamDashPtPass(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashptpass')
test = teamdashptreb.TeamDashPtReb(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashptreb')
test = teamdashptshots.TeamDashPtShots(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashptshots')
test = teamdashboardbyclutch.TeamDashboardByClutch(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbyclutch')
test = teamdashboardbygamesplits.TeamDashboardByGameSplits(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbygamesplits')
test = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbygeneralsplits')
test = teamdashboardbylastngames.TeamDashboardByLastNGames(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbylastngames')
test = teamdashboardbyopponent.TeamDashboardByOpponent(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbyopponent')
test = teamdashboardbyshootingsplits.TeamDashboardByShootingSplits(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbyshootingsplits')
test = teamdashboardbyteamperformance.TeamDashboardByTeamPerformance(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbyteamperformance')
test = teamdashboardbyyearoveryear.TeamDashboardByYearOverYear(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdashboardbyyearoveryear')
test = teamdetails.TeamDetails(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamdetails')
test = teamgamelog.TeamGameLog(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamgamelog')
test = teamgamestreakfinder.TeamGameStreakFinder().nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamgamestreakfinder')
test = teamhistoricalleaders.TeamHistoricalLeaders(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamhistoricalleaders')
test = teaminfocommon.TeamInfoCommon(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teaminfocommon')
test = teamplayerdashboard.TeamPlayerDashboard(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamplayerdashboard')
test = teamplayeronoffdetails.TeamPlayerOnOffDetails(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamplayeronoffdetails')
test = teamplayeronoffsummary.TeamPlayerOnOffSummary(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamplayeronoffsummary')
test = teamvsplayer.TeamVsPlayer(team_id='1610612739', vs_player_id='2544').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamvsplayer')
test = teamyearbyyearstats.TeamYearByYearStats(team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'teamyearbyyearstats')
test = videodetails.VideoDetails(player_id='2544', team_id='1610612739').nba_response.valid_json()
if not test:
    raise Exception('fail', 'videodetails')
test = videoevents.VideoEvents(game_id='0021700807').nba_response.valid_json()
if not test:
    raise Exception('fail', 'videoevents')
test = videostatus.VideoStatus().nba_response.valid_json()
if not test:
    raise Exception('fail', 'videostatus')
